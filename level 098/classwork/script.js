//1 
    let num=Math.floor(Math.random()*10)
    if (num%2===0){
        console.log(true)
    }
    else{
        console.log(false)
    }
//2
    let age=Math.floor(Math.random()*30)
    if(age<13){
        console.log("ბავშვი")
    }
    else if (age>=13 && age<=17){
        console.log("თინეიჯერი")
    }
    else{
        console.log("ზრდასრული")
    }
//3 
    let username="admin"
    let password="123"
    if(username==="admin" && password==="1234"){
        console.log("გილოცავთ თქვენ მოიგეთ 1000 robux")
    }
    else{
        console.log("თავიდან სცადე")
    }