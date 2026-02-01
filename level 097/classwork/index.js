// სამივე მათგანი ცვლადს ქმინს //
let Name="a" // დღეისათვის let უფრო ხშირად იყენებენ ვიდრე var ის უბრალოდ ქმნის ცვლადს

var Name1="b" /* var შედარებით ცუდი პრაქტიკაა რადგან როდესაც შენ ბევრი ინფორმაციის შნეხვა გინდა var ცვლადით ის ტვირთავს 
                საიტს ასევე თუ windows ში რომელიმე ცვლადის სახელი ემთხვევა var ცვლადის სახელს მაშინ windows ში მყოფ 
                (ავტომატურად შექმნილ ცვლადს) მნიშვნელობა შეეცვლება*/

const Name2="c" // const - constant ანუ ნიშნავს მუდმივას შენ მისი მნიშვნელობის შეცვლა არ შეგიძლია

console.log(Name)
console.log(Name1)
console.log(Name2)

Name=1
Name1=2
// Name2=3 // არ შეიძლება რადგან როგორც უკვე ვახსენე const მუდმივას ნიშნავს ანუ ის უცვლელია

console.log(Name)
console.log(Name1)
console.log(Name2)

let myNameIs="Giorgi"

//typeof ოპერატორს ჩვენ იმისთვის ვიყენებთ რომ გამოვიგოთ ცვლადის ტიპი

const mySurnameIs="Mikeladze"
const myAgeIs=13
const iAmBoy=true

console.log(typeof myNameIs)
console.log(typeof mySurnameIs)
console.log(typeof myAgeIs)
console.log(typeof iAmBoy)