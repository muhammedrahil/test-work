
from fileinput import filename
from dbconnection import *
from flask import *
import functools
from datetime import datetime
import time
import os

app = Flask(__name__)
app.secret_key = "key"


def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid"  not in session:
            return redirect("/")
        return func()
    return secure_function



@app.route("/")
def login():
    return render_template("admin/login.html")


@app.route("/getLogin", methods=['post'])
def getLogin():
    uname = request.form['uname']
    pwd = request.form['pwd']
    qry = "select * from login where username =%s and ecode=%s"
    vals = (uname, pwd)
    result = selectone(qry, vals)
    if result is None:
        return '''<script>alert ("Invalid UserName OR Password");window.location="/"</script>'''
    elif result[3] == 'director':
        session['lid'] = 'director'
        return '''<script>alert("Director Login Successfull");window.location="/admins"</script>'''
    elif result[3] == 'manager':
        session['lid'] = 'manager'
        return '''<script>alert("Manager Login Successfull");window.location="/admins"</script>'''
    elif result[3] == "employee":
        session['lid'] = 'employee'
        return '''<script>alert("Login Successfull");window.location="/employeepage"</script>'''
    elif result[3] == "coo":
        session['lid'] = 'coo'
        return '''<script>alert("Coo Login Successfull");window.location="/home_coo"</script>'''    
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect('/')


@app.route("/admins")
@login_required
def admins():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        return render_template("admin/home.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''



@app.route("/addEmployee")
@login_required
def addEmployee():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        return render_template("admin/addEmployee.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@app.route("/GetaddEmployee", methods=['post'])
@login_required
def GetaddEmployee():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    logqry = "INSERT INTO login VALUES (NULL,%s,%s,'employee')"
    logval = (ename, ecode)
    lid = iud(logqry, logval)
    qry = "INSERT INTO `employee` VALUES (NULL,%s,%s,%s,%s)"
    val = (ename, ecode, branch, str(lid))
    iud(qry, val)
    return '''<script>alert("New Employee Added Successfully");window.location="/addEmployee"</script>'''


@app.route("/ViewEmployee")
@login_required
def ViewEmployee():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        qry = "SELECT * FROM `employee` ORDER BY emp_id DESC"
        res = select(qry)
        return render_template("admin/viewEmployee.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@app.route("/Search_branch", methods=['post'])
@login_required
def Search_branch():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        branch = request.form['branch']
        qry = "SELECT * FROM `employee` WHERE `branch`=%s ORDER BY `employee`.`emp_id` DESC"
        res = selectall(qry, branch)
        return render_template("admin/SearchViewEmployee.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''



@app.route("/DeleteEmployee")
@login_required
def DeleteEmployee():
    id = request.args.get('id')
    qry = "DELETE employee ,login FROM `employee` join login on employee.loginid = login.loginid WHERE login.`loginid`=%s "
    iud(qry, id)
    return '''<script>alert("Deleted Successfully");window.location="/ViewEmployee"</script>'''


@app.route("/employeepage")
@login_required
def employeepage():
    if(session['lid']== 'employee'):
        return render_template("employee/home.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''



@app.route("/SearchEmployee")
@login_required
def SearchEmployee():
    if(session['lid']== 'employee'):
        qry = "SELECT * FROM `employee`"
        res = select(qry)
        return render_template("employee/SearchEmployye.html", val=res)
    else :
         return '''<script>alert("Unavailable");window.history.back()</script>'''

 
@app.route("/ajaxpost",methods=["POST","GET"])
def ajaxpost():    
    if request.method == 'POST':
        queryString = request.form['queryString']
        query = "SELECT emp_name from employee WHERE emp_name LIKE '{}%' LIMIT 10".format(queryString)
        employee = select(query)
        employee = list(employee[0])
        
    return jsonify({'htmlresponse': render_template('employee/response.html', employee=employee)})



@app.route("/getvalSearchEmployee", methods=['post'])
@login_required
def getvalSearchEmployee():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    qry = "SELECT `employee`.*,`login`.* FROM `login` JOIN `employee` ON `employee`.`loginid`=`login`.`loginid` WHERE `employee`.`emp_name`=%s AND `employee`.`e-code`=%s AND `employee`.`branch`=%s"
    val = (ename, ecode, branch)
    result = selectone(qry, val)
    if result is None:
        return '''<script>alert ("Invalid ");window.location="/SearchEmployee"</script>'''
    elif result[8] == "employee":
        session['eid'] = result[4]
        return '''<script>alert("Thank you! Please Request Your Leave");window.location="/leaveRequestPage"</script>'''
    else:
        return '''<script>alert("invalid ");window.location="/SearchEmployee"</script>'''


@app.route("/leaveRequestPage")
@login_required
def leaveRequestPage():
    if(session['lid']== 'employee'):
        return render_template("employee/leaveRequest.html")
    else :
         return '''<script>alert("Unavailable");window.history.back()</script>'''



@app.route("/GetLeaveRequest", methods=['post'])
@login_required
def GetLeaveRequest():
    t = "17:00:00"
    test_time = datetime.strptime(t, '%H:%M:%S')
    current_time = datetime.now().strftime("%H:%M:%S")
    current_time = datetime.strptime(current_time, "%H:%M:%S")
    if(test_time.time() > current_time.time()):
        LRid = session['eid']
        reason = request.form['reason']
        date = request.form['date']
        expdate = request.form['expdate']
        if(reason == 'others'):
            reason = request.form['discription']
        qry = "INSERT INTO `leaverequest` VALUES (NULL,%s,'pending',%s,%s,%s,CURDATE())"
        val = (reason, LRid, date, expdate)
        iud(qry, val)
        return '''<script>alert("leave request successfull");window.location="/employeepage"</script>'''
    else:
        return '''<script>alert("Not Approved");window.location="/employeepage"</script>'''


@ app.route("/ViewReaqusetEmployee")
@login_required
def ViewReaqusetEmployee():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE `leaverequest`.`status`='pending'  ORDER BY `leaverequest`.`LRid` DESC"
        res = select(qry)
        return render_template("admin/viewLeaveRequest.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/Search_branch_Leave", methods=['post'])
@login_required
def Search_branch_Leave():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE `leaverequest`.`status`='pending' AND `employee`.`branch`=%s ORDER BY `leaverequest`.`LRid` DESC"
        res = selectall(qry, branch)
        return render_template("admin/Search_branch_Leave.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/Search_branch_Leave_accepted", methods=['post'])
@login_required
def Search_branch_Leave_accepted():
    if(session['lid']== 'manager' or session['lid']== 'director'):    
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE `leaverequest`.`status`='Accepted' AND `employee`.`branch`=%s ORDER BY `leaverequest`.`LRid` DESC"
        res = selectall(qry, branch)
        return render_template("admin/accept_list.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/AcceptReaqusetEmployee")
@login_required
def AcceptReaqusetEmployee():
    accept = "Accepted"
    id = request.args.get('id')
    session['id'] = id
    qry = "update`leaverequest` set `status`=%s WHERE LRid =%s"
    val = (accept, session['id'])
    iud(qry, val)
    return '''<script>window.location="/ViewReaqusetEmployee"</script>'''


@ app.route("/accept_list_leave")
@login_required
def accept_list_leave():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE `leaverequest`.`status`='Accepted'  ORDER BY `leaverequest`.`LRid` DESC"
        res = select(qry)
        return render_template("admin/accept_list.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/rejectReaqusetEmployee")
@login_required
def rejectReaqusetEmployee():
    reject = "Rejected"
    id = request.args.get('id')
    session['id'] = id
    qry = "update`leaverequest` set `status`=%s WHERE LRid =%s"
    val = (reject, session['id'])
    iud(qry, val)
    return '''<script>alert("rejected successfully");window.location="/ViewReaqusetEmployee"</script>'''


@ app.route("/SetEmployeestarget")
@login_required
def SetEmployeestarget():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        qry = "SELECT `login`.*,`employee`.* FROM `login`JOIN`employee`ON`login`.`loginid`=`employee`.`loginid` ORDER BY `employee`.`emp_id` DESC"
        res = select(qry)
        return render_template("admin/setTarget.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/Search_branch_SetTarget", methods=['post'])
@login_required
def Search_branch_SetTarget():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        branch = request.form['branch']
        qry = "SELECT `login`.*,`employee`.* FROM `login`JOIN`employee`ON`login`.`loginid`=`employee`.`loginid` WHERE `employee`.`branch`=%s ORDER BY `employee`.`emp_id` DESC"
        res = selectall(qry, branch)
        return render_template("admin/Search_branch_SetTarget.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/SettargetEmployees")
@login_required
def SettargetEmployees():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        id = request.args.get('id')
        session['id'] = id
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON `employee`.`loginid`=`target`.`lg_id` WHERE `employee`.`loginid`=%s"
        res = selectone(qry, id)
        if(res == None):
            return render_template("admin/target.html", val=res)
        else:
            return '''<script>alert("already set, Please update employee target");window.location="/viewupdatetargetEmployees"</script>'''
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''
        

@ app.route("/GettargetEmployees", methods=['post'])
@login_required
def GettargetEmployees():
    Gold = request.form['Gold']
    Diamond = request.form['Diamond']
    qry = "INSERT INTO `target` VALUES (NULL,%s,%s,%s,%s,%s)"
    val = (Gold, session['id'], 00, Diamond, 00)
    iud(qry, val)
    return '''<script>window.location="/SetEmployeestarget"</script>'''


@ app.route("/viewupdatetargetEmployees")
@login_required
def viewupdatetargetEmployees():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON employee.`loginid`=`target`.`lg_id` ORDER BY `target`.`trid` DESC"
        res = select(qry)
        return render_template("admin/ViewtargetEmp.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/Search_viewupdatetargetEmployees", methods=['post'])
@login_required
def Search_viewupdatetargetEmployees():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON employee.`loginid`=`target`.`lg_id`  WHERE `employee`.`branch`=%s ORDER BY `employee`.`emp_id` DESC"
        res = selectall(qry, branch)
        return render_template("admin/Search_viewupdatetargetEmployees.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/updateEmployeestarget")
@login_required
def updateEmployeestarget():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        id = request.args.get('id')
        session['tid'] = id
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON employee.`loginid`=`target`.`lg_id` where `target`. `trid`=%s "
        res = selectone(qry, id)
        return render_template("admin/updateTarget.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/GetupdatetargetEmployees", methods=['post'])
@login_required
def GetupdatetargetEmployees():
    Gold = request.form['Gold']
    Diamond = request.form['Diamond']
    qry = "UPDATE `target` SET `gold`=%s ,`Diamond`=%s WHERE trid =%s"
    val = (Gold, Diamond, session['tid'])
    iud(qry, val)
    return '''<script>window.location="/viewupdatetargetEmployees"</script>'''


@ app.route("/AchiveEmployeestarget")
@login_required
def AchiveEmployeestarget():
    if(session['lid']== 'manager' or session['lid']== 'director'):
        id = request.args.get('id')
        session['tid'] = id
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON employee.`loginid`=`target`.`lg_id` where `target`. `trid`=%s "
        res = selectone(qry, id)
        return render_template("admin/Achive.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/GetAchiveEmployeestarget", methods=['post'])
@login_required
def GetAchiveEmployeestarget():
    Gold = request.form['Gold']
    Diamond = request.form['Diamond']
    qry = "UPDATE target SET `achive_gold`=%s,`achive_diamond`=%s WHERE trid =%s"
    val = (Gold, Diamond, session['tid'])
    iud(qry, val)
    return '''<script>window.location="/viewupdatetargetEmployees"</script>'''


@ app.route("/SearchTargetEmployeeView")
@login_required
def SearchTargetEmployeeView():
    if(session['lid']== 'employee'):
        return render_template("employee/SearchTargetEmployeeView.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''



@ app.route("/getvalTargetSearchEmployee", methods=['post'])
@login_required
def getvalTargetSearchEmployee():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    qry = "SELECT `employee`.*,`login`.* FROM `login` JOIN `employee` ON `employee`.`loginid`=`login`.`loginid` WHERE `employee`.`emp_name`=%s AND `employee`.`e-code`=%s AND `employee`.`branch`=%s"
    val = (ename, ecode, branch)
    result = selectone(qry, val)
    if result is None:
        return '''<script>alert ("invalid");window.location="/SearchTargetEmployeeView"</script>'''
    elif result[8] == "employee":
        session['rid'] = result[4]
        return '''<script>alert("Thank you , Please View Your Target And Achived Target ");window.location="/ViewEmployeeTargetList"</script>'''
    else:
        return '''<script>alert("invalid ");window.location="/SearchTargetEmployeeView"</script>'''


@ app.route("/ViewEmployeeTargetList")
@login_required
def ViewEmployeeTargetList():
    if(session['lid']== 'employee'):
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON `employee`.`loginid`=`target`.`lg_id` WHERE `employee`.`loginid`=%s"
        res = selectone(qry, session['rid'])
        return render_template("employee/ViewEmployeeTargetList.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/ViewLeaveRequest_statusPages")
@login_required
def ViewLeaveRequest_statusPages():
    if(session['lid']== 'employee'):
        return render_template("employee/ViewLeaveRequest.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/GetViewLeaveRequestPage", methods=['post'])
@login_required
def GetViewLeaveRequestPage():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    qry = "SELECT `employee`.*,`login`.* FROM `login` JOIN `employee` ON `employee`.`loginid`=`login`.`loginid` WHERE `employee`.`emp_name`=%s AND `employee`.`e-code`=%s AND `employee`.`branch`=%s"
    val = (ename, ecode, branch)
    result = selectone(qry, val)
    if result is None:
        return '''<script>alert ("Invalid");window.location="/ViewLeaveRequest_statusPages"</script>'''
    elif result[8] == "employee":
        session['rid'] = result[4]
        return '''<script>alert("Thank you, Please View Your Leave Request Status");window.location="/viewLeaveRequestPage"</script>'''
    else:
        return '''<script>alert("invalid ");window.location="/ViewLeaveRequest_statusPages"</script>'''


@ app.route("/viewLeaveRequestPage")
@login_required
def viewLeaveRequestPage():
    if(session['lid']== 'employee'):
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE  `employee`.`loginid`= %s ORDER BY `leaverequest`.`LRid` DESC"
        res = selectall(qry, session['rid'])
        return render_template("employee/viewLeaveRequestPage.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/StatusviewLeaveRequest")
@login_required
def StatusviewLeaveRequest():
    id = request.args.get('id')
    qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id`WHERE`leaverequest`.`LRid`=%s"
    res = selectone(qry, id)
    return render_template("employee/ViewEmployeeLeaveList.html", val=res)


@ app.route("/SearchPymentPage")
@login_required
def SearchPymentPage():
    if(session['lid']== 'employee'):
        return render_template("employee/SearchPyment.html")
    else :
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/GetSearchPymentPage", methods=['post'])
@login_required
def GetSearchPymentPage():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    qry = "SELECT `employee`.*,`login`.* FROM `login` JOIN `employee` ON `employee`.`loginid`=`login`.`loginid` WHERE `employee`.`emp_name`=%s AND `employee`.`e-code`=%s AND `employee`.`branch`=%s"
    val = (ename, ecode, branch)
    result = selectone(qry, val)
    if result is None:
        return '''<script>alert ("Invalid");window.location="/SearchPymentPage"</script>'''
    elif result[8] == "employee":
        session['rid'] = result[4]
        return '''<script>alert("Thank you,Please Request Your Pyment");window.location="/PymentPage"</script>'''
    else:
        return '''<script>alert("Invalid ");window.location="/SearchPymentPage"</script>'''


@ app.route("/PymentPage")
@login_required
def PymentPage():
    if(session['lid']== 'employee'):
        return render_template("employee/pymentPage.html")
    else:
         return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/GetPymentPage", methods=['post'])
@login_required
def GetPymentPage():
    PymentOption = request.form['PymentOption']
    pyment = request.form['pyment']
    if (PymentOption == "others"):
        PymentOption = request.form['discription']
    qry = "INSERT INTO `pyment` VALUES (NULL,%s,%s,%s,'pending',CURDATE())"
    val = (PymentOption, pyment, session['rid'])
    iud(qry, val)
    return '''<script>alert("Payment Request Succesfully");window.location="/employeepage"</script>'''


@ app.route("/BranchEmployeePymentPage")
@login_required
def BranchEmployeePymentPage():
    if(session['lid']== 'director'):
        qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id` WHERE`pyment`.`status`='pending' ORDER BY `pyment`.`pid` DESC"
        res = select(qry)
        return render_template("maneger/viewPymentEmployee.html", val=res)
    else:
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/Search_branch_Pyment", methods=['post'])
@login_required
def Search_branch_Pyment():
    if(session['lid']== 'director'):
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id` WHERE`pyment`.`status`='pending' AND `employee`.`branch`=%s ORDER BY `pyment`.`pid` DESC"
        res = selectall(qry, branch)
        return render_template("maneger/Search_branch_Pyment.html", val=res)
    else:
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/Search_branch_Pyment_accepted", methods=['post'])
@login_required
def Search_branch_Pyment_accepted():
    if(session['lid']== 'director'):
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id` WHERE`pyment`.`status`='Accepted' AND `employee`.`branch`=%s ORDER BY `pyment`.`pid` DESC"
        res = selectall(qry, branch)
        return render_template("maneger/accept_list.html", val=res)
    else:
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/AcceptBranchEmployeePymentPage")
@login_required
def AcceptBranchEmployeePymentPage():
    accept = "Accepted"
    id = request.args.get('id')
    qry = "update pyment set `status`=%s WHERE pid =%s"
    val = (accept, id)
    iud(qry, val)
    return '''<script>alert("accepted successfully");window.location="/BranchEmployeePymentPage"</script>'''


@ app.route("/rejectBranchEmployeePymentPage")
@login_required
def rejectBranchEmployeePymentPage():
    reject = "Rejected"
    id = request.args.get('id')
    qry = "update pyment set `status`=%s WHERE pid =%s"
    val = (reject, id)
    iud(qry, val)
    return '''<script>alert("rejected successfully");window.location="/BranchEmployeePymentPage"</script>'''


@ app.route("/EditBranchEmployeePymentPage")
@login_required
def EditBranchEmployeePymentPage():
    if(session['lid']== 'director'):
        id = request.args.get('id')
        session['pid'] = id
        qry = "SELECT * FROM `pyment` WHERE`pid`=%s"
        res = selectone(qry, id)
        return render_template("maneger/EditPyment.html", val=res)
    else:
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/GetEditBranchEmployeePymentPage", methods=['post'])
@login_required
def GetEditBranchEmployeePymentPage():
    money = request.form['number']
    qry = "update pyment set `moneny`=%s WHERE pid =%s"
    val = (money, session['pid'])
    iud(qry, val)
    return '''<script>alert("Edit successfully");window.location="/BranchEmployeePymentPage"</script>'''


@ app.route("/SearchViewPayment_Status")
@login_required
def SearchViewPayment_Status():
    if(session['lid']== 'employee'):
        return render_template("employee/SearchViewPayment.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/GetSearchViewPayment", methods=['post'])
@login_required
def GetSearchViewPayment():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    qry = "SELECT `employee`.*,`login`.* FROM `login` JOIN `employee` ON `employee`.`loginid`=`login`.`loginid` WHERE `employee`.`emp_name`=%s AND `employee`.`e-code`=%s AND `employee`.`branch`=%s"
    val = (ename, ecode, branch)
    result = selectone(qry, val)
    if result is None:
        return '''<script>alert ("Invalid");window.location="/SearchViewPayment_Status"</script>'''
    elif result[8] == "employee":
        session['rid'] = result[4]
        return '''<script>alert("Thank you, Please View Your Payment Status");window.location="/listPymentListseployee"</script>'''
    else:
        return '''<script>alert("Invalid");window.location="/SearchViewPayment_Status"</script>'''


@ app.route("/listPymentListseployee")
@login_required
def listPymentListseployee():
    if(session['lid']== 'employee'):
        qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id` WHERE `employee`.`loginid`=%s ORDER BY `pyment`.`pid` DESC"
        res = selectall(qry, session['rid'])
        return render_template("employee/listPymentListseployee.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/StatusviewlistPymentListseployee")
@login_required
def StatusviewlistPymentListseployee():
    if(session['lid']== 'employee'):
        id = request.args.get('id')
        qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id`  WHERE `pyment`.`pid`=%s"
        res = selectone(qry, id)
        return render_template("employee/SearchViewPaymentList.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/StatusviewlistPymentListsmanager")
@login_required
def StatusviewlistPymentListsmanager():
    if(session['lid']== 'director'):
        id = request.args.get('id')
        qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id`  WHERE `pyment`.`pid`=%s"
        res = selectone(qry, id)
        return render_template("maneger/SearchViewPaymentList.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/accept_list")
@login_required
def accept_list():
    qry = "SELECT `employee`.*,`pyment`.* FROM `pyment` JOIN `employee` ON `employee`.`loginid`=`pyment`.`lg_id` WHERE`pyment`.`status`='Accepted' ORDER BY `pyment`.`pid` DESC"
    res = select(qry)
    return render_template("maneger/accept_list.html", val=res)


@ app.route("/memo_page")
@login_required
def memo_page():
    return render_template("admin/memo.html")


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


@ app.route("/Get_memo_page", methods=['GET', 'POST'])
@login_required
def Get_memo_page():
    upload_file = request.files['files']
    file_name = upload_file.filename
    Discription = request.form['Discription']
    upload_file.save(upload_file.filename)
    file = convertToBinaryData(upload_file.filename)
    qry = "INSERT INTO `memo` VALUES(NULL,%s,%s,%s)"
    val = (Discription, file, file_name)
    iud(qry, val)
    return '''<script>alert("Memo Added Successfully");window.location="/memo_page"</script>'''


@ app.route("/memo_list")
@login_required
def memo_list():
    qry = "Select * From memo ORDER BY `memoid` DESC"
    res = select(qry)
    return render_template("admin/Memo_List.html", val=res)


@ app.route("/Delete_memo")
@login_required
def Delete_memo():
    id = request.args.get('id')
    qry = "DELETE FROM `memo` WHERE `memoid`=%s"
    res = iud(qry, id)
    return '''<script>alert("Deleted Successfully");window.location="/memo_list"</script>'''


def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def Remove(filename):
    time.sleep(3)
    os.remove(filename)


@app.route("/download_file")
@login_required
def download_file():
    id = request.args.get('id')
    qry = "select * from memo WHERE `memoid`=%s"
    res = selectone(qry, id)
    print("Id = ", res[0], )
    print("discription = ", res[1])
    file = res[2]
    filename = res[3]
    write_file(file, filename)
    return send_file(filename,
                     attachment_filename=filename,
                     as_attachment=True)
                     


@ app.route("/memo_list_employee")
@login_required
def memo_list_employee():
    if(session['lid']== 'employee'):
        qry = "Select * From memo ORDER BY `memoid` DESC"
        res = select(qry)
        return render_template("employee/Memo_List.html", val=res)
    else : 
         return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/home_coo")
@login_required
def home_coo():
    if(session['lid']== 'coo'):
        return render_template("coo/home.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/accept_list_leave_coo")
@login_required
def accept_list_leave_coo():
    if(session['lid']== 'coo'):
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE `leaverequest`.`status`='Accepted'  ORDER BY `leaverequest`.`LRid` DESC"
        res = select(qry)
        return render_template("coo/accept_list.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/Search_branch_Leave_coo", methods=['post'])
@login_required
def Search_branch_Leave_coo():
    if(session['lid']== 'coo'):
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`leaverequest`.* FROM `leaverequest` JOIN `employee` ON `employee`.`loginid`=`leaverequest`.`lg_id` WHERE `leaverequest`.`status`='Accepted' AND `employee`.`branch`=%s ORDER BY `leaverequest`.`LRid` DESC"
        res = selectall(qry, branch)
        return render_template("coo/Search_branch_Leave.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/viewupdatetargetEmployees_coo")
@login_required
def viewupdatetargetEmployees_coo():
    if(session['lid']== 'coo'):
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON employee.`loginid`=`target`.`lg_id` ORDER BY `employee`.`emp_id` DESC"
        res = select(qry)
        print(res)
        return render_template("coo/ViewtargetEmp.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/Search_viewupdatetargetEmployees_coo", methods=['post'])
@login_required
def Search_viewupdatetargetEmployees_coo():
    if(session['lid']== 'coo'):
        branch = request.form['branch']
        qry = "SELECT `employee`.*,`target`.* FROM `target` JOIN `employee` ON employee.`loginid`=`target`.`lg_id`  WHERE `employee`.`branch`=%s ORDER BY `employee`.`emp_id` DESC"
        res = selectall(qry, branch)
        return render_template("coo/Search_viewupdatetargetEmployees.html", val=res)
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''

@ app.route("/manager_leave_Request")
@login_required
def manager_leave_Request():
    if(session['lid']== 'manager'):
        return render_template("maneger/leaveRequest.html")
    else : 
        return '''<script>alert("Unavailable");window.history.back()</script>'''


@ app.route("/get_manager_leave_Request", methods=['GET', 'POST'])
@login_required
def get_manager_leave_Request():
    ename = request.form['ename']
    ecode = request.form['ecode']
    branch = request.form['branch']
    reason = request.form['reason']
    date = request.form['date']
    expdate = request.form['expdate']
    if(reason == 'others'):
        reason = request.form['discription']
    qry = "SELECT `employee`.* FROM `employee`  WHERE `emp_name`=%s AND `e-code`=%s AND `branch`=%s"
    val=(ename,ecode,branch)  
    res=selectone(qry,val)
    id=res[4] 
    qry1 = "INSERT INTO `leaverequest` VALUES (NULL,%s,'Accepted',%s,%s,%s,CURDATE())"
    val1 = (reason, id, date, expdate)
    iud(qry1, val1)
    return '''<script>alert(" Successfull");window.location="/manager_leave_Request"</script>'''

if __name__ == "__main__":
    app.run(debug=True)
