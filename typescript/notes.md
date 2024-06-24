# Typescript notes :-

## to run a trypscript file in watch mode or auto-compiliation use:

```bash
yarn tsc main.ts -w
```

## tsconfig.json file:

the tsconfig file have all the settings of typescript.

### to change the output dir of compilied typescript file change:-

"outDir": "./folder name",
all the compilied typescript file will be present in outdir

### to change the root dir :-

"rootDir": "./",

## to declare any type use:

let name : string = "name"

## functions in typescript

```typescript
const sum = (a: number, b: number) => {
  return a + b;
};

console.log(sum(7, 7));
```

### defining multiple types

const a:number | string ;

RegExp is type of regular expression when using regexp

# chapter 3 Arrays and Object

## to declare array with restricted array use:

```ts
let details: [string, number, boolean] = ["deepak", 7, true];
console.log(details);
```

## how to define types :

```ts
type det = {
  name: string;
  rollno: number;
  marks: (number | boolean)[];
};

let details: det = {
  name: "deepak kahar",
  rollno: 7,
  marks: [50, 60, true],
};

console.log(details);
```

we can put ? to the type to make optional for the data type

# Chapter 4 Functions

## Type Alieas

the type alias define what kind of data value is available on a variable

for eg:-

```typescript
type StringOrNumber = string | number;

type StringOrNumberArray = (string | number)[];

type student_details = {
  name: string;
  rollno: number;
  isPresent?: boolean; //optional datatypes
  marks: StringOrNumber;
};
```

## Literal Types

the literal types provide what value should be assigned to a variable

```typescript
let world: "earth" | "venus" | "mars";

world = "venus";
console.log(world);
```

## Functions

the functions parameters have a type and it can also define the return type

```typescript
const add = (a: number, b: number) => {
  return a + b;
};

const message = (msg: any): void => {
  return msg;
};

console.log(add(5, 5));
console.log(message("007"));
```

# chapter 5 - Type Assertions

type asserations and type casting are same.

## as keyword

we can use as keyword to tell typescript that this value gonna return what i told it.

```typescript
const addOrConcat = (
  a: number,
  b: number,
  c: "add" | "concate"
): string | number => {
  if (c === "add") return a + b;
  return " " + a + b;
};

let myVal: string = addOrConcat(3, 5, "concate") as string;
console.log(myVal);
```

## unknown type

the unknown type used when you want to cast something and from number to string but it is not recommended
10 as string;
10 as unknown as string;

but it can be very usefull in DOM

# class

when defining a class all the properties of class must be availabe in contructor.

```ts
class User{
  name:string,
  age: number
    constructor(name:string,age:number){
      this.name=name,
      this.age=age
    }
}
// to insert data and print
const detail = new User("deepak", 34);
console.log(detail);
```

## Access Modifier :

public , private, protected, readonly
these modifier can be use as oops class.(by default all members are public)

## interface implements:

```ts
interface details {
  msg: string;
}
class say implements details {
  msg: string;
  constructor(msg: string) {
    this.msg = msg;
  }
  public greet() {
    return `hello everyone ${this.msg}`;
  }
}
const s = new say("don't say anything");
console.log(s.greet());
```

Read about static, getter , setter in ts-documenttaion

# ch-7 index signatures and keyof assertions

to define index signature:

```ts
type transaction = {
  [key: string]: number | string;
};
const newTransaction: transaction = {
  title: "pizza",
  amount: 5000,
};
console.log(newTransaction.title);
```

# Generics Type:

generics type use when you don't know what kind of value you are gone send to function and what it will return.

```ts
const msg = <T>(arg: T): T => arg;
console.log(msg("hi"));
```
