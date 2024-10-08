# Javascript Notes:

## Table of Content

1. [Basics of Javascript](#basics-of-javascript)
   - [variables](#variables)
   - [data types](#datatypes)
     - [datatype conversion](#datatype-conversion)
   - [math and number](#number-and-math-operations)
   - [Date and time](#date-and-time)
   - [array](#array-in-javascript)
     - [array in depth](#array-part-2)
   - [object](#objects)
     - [objects in depth](#object-in-depth)
   - [global and local scopes](#global-and-local-scopes)

## Basics of javascript

### variables

to create variable in ajavascript use const, let, var. it wil occupy a spcae in memory to store data.

```js
const accountId = "Ax34534534"; // constantvaraible cannot change the value
let email = "email@gmail.com"; // scope level value can be change by other methods
var age = 56; // global level scope ( never use )

city = "my city"; // you can define variable without using const or let
// but avoid this

let hometown; // a variable without assigned value is undefiend

console.log(accountId); // print variable value in console
console.table([accountId, email, age]); // print value in tablur form
```

### datatypes

datatypes are the type of value a variable can store.

```js
"use strict"; // this will use to use newer version of javascript

//  Primitve data types;

// string = " value "
// number = 345345
// bigint = hold value bigger than number
// boolean = true , false
// null = standalone value
// undefined = vriable created but value not assigned
// symbol = to creating uniqueness

// to check a data type of variable use :
console.log(typeof "hello"); // return string
console.log(typeof age); //return number
```

### datatype conversion

there are many javascript functions that can convert values is called conversion.

```js
let num1 = "45"
console.log(typeof(num1)) // string

let converted_Num1 = Number(num1) // converting value
console.log(typeof converted_Num1) // number

// other values to convert
"45" => 45 // converted to a number
"45as" => NaN // not converted
null => NaN // not a number
undefined => NaN // not changed
true => 1 //change to 1
```

many conversion are available in js;

- Number() // convert to number
- String() // convert to string
- Boolean() // convert to boolean

### number and math operations

- Numbers

```js
const number_1 = 45; // assigning number value

const number_2 = new Number(56); // uesing number constructor
console.table([number_1, number_2]);

console.log(number_2.toString().length); // 45 = string
// to chnage number to string, after that have all he method of string

console.log(number_1.toFixed(2)); // 45.00
// to have a decimal value

const otherNumber = 4345.76243;
console.log(otherNumber.toPrecision(3)); // gets the number after decimal, if the value is bigger than precision value then it gets a round off. always return string

const currency = 1000000;
console.log(currency.toLocaleString("en-IN")); // 10,00,000
// convert it to loale string default is US standard

console.log(currency.toLocaleString("en-IN")); // for indian standard
```

- Maths

math function is usefull when ou want to work with math or any formula.

```js
console.log(Math.abs(-656)); // 656 in positive
// chnage negative value to positive

console.log(Math.round(5623.67)); // 5623
// round off value

console.log(Math.ceil(67.2)); // 68
// return top value

console.log(Math.floor(67.8)); // 67
//return lowest value

console.log(Math.random()); // 0.5345345
// return value between 0 - 1 in decimal

console.log(Math.random() * 10 + 1);
// return value between 1 - 10 except 0
```

**to generate a random number betwee a range use this formula**

```js
const max = 20;
const min = 10;

console.log(Math.floor(Math.random() * (max - min + 1) + min));

//generate a random nuber between 10 to 20
```

### date and time

the date object

```js
const date = new Date();

console.log(typeof date); // object type
console.log(date.toString()); // return time in string
console.log(date.toDateString()); // return date,day
console.log(date.toLocaleDateString()); // date

let newDate = new Date(2023, 2, 12);
console.log(newDate);
console.log(newDate.toString());
```

### array in javascript

```js
const array = [1, 2, 3, 4, 5];
console.log(array[3]); // indexing of array
array.push(45); // add a value at the end
array.pop(); // remove last value
array.unshift(90); // add va;ue at the starting of array and shift the indexing
array.shift(); // remove first value of array
console.log(array.includes(45)); // cherck the value exist in array or not, return boolean

console.log(array.indexOf(3)); // return th index of value

const new_Array = [45, 56, 67];
const result = new_Array.join(); // create a string of array value
console.log(typeof result, result);
const my_array = new_Array.slice(1, 3); // [ 56,67 ]
// return a value of index
const my_array = new_Array.splice(1, 3); // [56,67]
// return the index value of array and change the array

console.log(my_array, new_Array);
```

### array part 2

```js
const first_Array = [1, 2, 3];
const sec_Array = ["hello", "world", false];

const result = sec_Array.push(first_Array); // added value inside the exisitng array

const result = first_Array.concat(sec_Array); // add two or more array and return new array

const result = [...first_Array, ...sec_Array]; // modern syntax for adding two array

const nested_Array = [1, 2, 3, [4, 5, 6], 7, [8, [9, 10]]];

const result = nested_Array.flat(2); // [1,2,3,4,5,6,7,8,9,10]
// return avlue inside a new array with all value recursively
// depth = how much nested array to open

const result = nested_Array.flat(Infinity); // open all depth inside a array

const result = Array.isArray("hello"); // false
// to check a value is array or not

const result = Array.from("hello"); // [ 'h', 'e', 'l', 'l', 'o' ]
// change any value to array

let score = 100;
let score2 = 200;
let score3 = 300;

const result = Array.of(score, score2, score3); // [100,200,300]
// create a new array with multiple values

console.log(result);
```

### objects

there are two ways to create objects in javascript

1. singleton = only 1 instance of its own, and only created by **Object constructor**.
2. literal = whenever we create onject using const,var, let , it will create literal type

there are basically two ways to access value of object

```js
const person = {
  name: "name 1",
  age: 34,
  marks: [23, 45, 56, 78],
  isAdult: true,
};

console.log(person.name); // name 1
console.log(person["name"]); // name 1
// another way to access object value, eg:
// const person={"name":"name1"}
```

if you want to use symbol inside a object use:

```js
const obj = {
  mySymbol: Symbol("key1"), // defining symbol
};

// or use

const mySymbol = Symbol("key1");

const obj = {
  [symbol]: "key1",
};

//accessing the value of symbol use
console.log(person[symbol]);

// freezing object
// Object.freeze(person); // freezing a object, it mean no changes in any value inside the object, don't show any error but you won't be able to chage value
// person.name = "hello"; // value not chnaged
```

### object in depth

```js
const user = {
  email: "eg@gmail.com",
  fullName: {
    first: "first name",
    last: "last name",
  },
};

console.log(user.fullName?.first); // optional chaining

const obj = { 1: "1", 2: "2" };
const obj2 = { 3: "3", 4: "4" };
const obj3 = { 5: "5", 6: "6" };

const new_Obj = Object.assign({}, obj, obj2, obj3); //merge multiple object into new empty object

const new_Obj = { ...obj, ...obj2, ...obj3 };
// another way to merge multiple object

const new_Obj = Object.keys(user);
// return a array with all keys of object

const new_Obj = Object.values(user);
// return a array with values of object

const new_Obj = Object.entries(user);
// return a array with all values enumerable

const new_Obj = Object.hasOwnProperty("log");
// return boolean that a key is available in a objet or not

console.log(new_Obj);
```

### global and local scopes

```js
if (true) {
  let num = 10;
  const num2 = 20;
  var num3 = 30; // global scope var
}

console.log(num3);
```

### scope level and hoisting

```js
function one() {
  let first = "frist name";
  function two() {
    let second = "second name";
    console.log(second);
  }
  two();
}

one();

/////////////////////////////////
print();

function print() {
  // simple function decalration
  console.log("print runnning");
}

printTwo(); // throw a error

const printTwo = function two() {
  // variable holding a function
  console.log("two pring");
};
```

**difference between normal function decalration and a function holding a variable**

normal : the normal function can be called before the initialization.

variable funcation : but the variable functins cann not run before initalization

### imediatily invoke function

these functions immediatly invoke or called while declared.

```js
(function print() {
  console.log("print running");
})(); // wrap inside the pranthesis to use IIFE

////////////////////
// Arrow functions
(() => {
  console.log("running two");
})();

/////////////////\

// with arguments

((value) => {
  console.log("the value is ", value);
})(56);
```

### How does JS works ?

javascript execution context

- global execution context like - this,
- function execution context =
- eval execution context

Memory creation phase,
this phase only include memory allocation, asigning variable, values.
**no code execution , by deffault all value assign with undefined value**

Execution Phase
all execution of code start here

### loops and iteration

- for loops

```js
const num = 2;
for (let i = 1; i <= 10; i++) {
  if (i == num) {
    console.log(`value find at ${i} index`);
  }
  continue;
}

/////////////////
// another eg
const how = 5;

for (let i = 1; i <= how; i++) {
  for (let j = 1; j <= 10; j++) {
    console.log(`${i} * ${j * i}`);
  }
}
```

- for of loops

for of loop can be use with any value like, array, object, string

```js
const heros = ["batman", "joker", "green"];

for (const value of heros) {
  console.log(value);
}
```

- map

the maps are the unique key value pair object

```js
const map = new Map();
map.set("in", "india");
map.set("fr", "france");
map.set("usa", "unioted");

console.log(typeof map, map);

//////////////////////
// loop the map

for (const [key, value] of map) {
  console.log(key, ";", value);
}
```

- for in loops

the for in loop uses the key of a iterator

```js
const user = {
  name: "hello",
  age: 56,
  city: "new delhi",
};

for (const i in user) {
  console.log(i); // keys
  console.log(user[i]); // value
}
```

**the major differnce between for of and for in loops is that for run on value and for in loop on key**

### map, filter, for-each and reduce

- for-each function for array

it will not return any value so you won't be able to save in any variable

```js
// not allowed
// const all = heros.forEach((h) => console.log(h));

const heros = ["batman", "joker", "green"];
heros.forEach((h) => console.log(h));

////////////////////////////////////
// it have its own property like index, and array

// h = current value
// index = current index
// arr = complete array

heros.forEach((h, index, arr) => {
  console.log(`${h} - ${index}`);
  console.log(arr);
});
```

- filter

in filter it always return a new array that matched the condition

```js
const random = [1, 2, 3, 4, 5, 6, 7, 8];
const even = random.filter((v) => v % 2 == 0);
console.log(even);

///////////////////////////
// check multiple condition with scope
const random = [1, 2, 3, 4, 5, 6, 7, 8];

const even = random.filter((v) => {
  return v % 2 == 0 && v > 5;
});
```

- Map

the map is works same as filter but no condition only loops throught

```js
const random = [1, 2, 3, 4, 5, 6, 7, 8];
const number = random.map((v) => v + 10);
console.log(number);
```

- chaining multiple array method

you can chain multiple method of array togather like, map,filter, inside map

```js
const random = [1, 2, 3, 4, 5, 6, 7, 8];
const number = random.map((v) => v * 20).filter((v) => v >= 50);

console.log(number);
```

- Reduce (important)

the reduce method have two default values,

- prev = previous value of array
- curr = current value of array

```js
const random = [1, 2, 3, 4, 5, 6, 7, 8];
const number = random.reduce((prev, curr) => prev + curr); // 36

console.log(number);

// add all the value of array and return total value
```

in reduce method you can also define initial value, of previous value, by default 0.

```js
const random = [1, 2, 3, 4, 5, 6, 7, 8];

const number = random.reduce((prev, curr) => {
  return prev + curr;
}, 4); // 40

console.log(number);
```
