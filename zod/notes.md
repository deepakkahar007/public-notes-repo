# ZOD Tutorial

1. [installation](#installation)
2. [basic usage](#basic-usage)
3. [infer](#infer-with-zod-type)
4. [parse method](#parse-method)
5. [safe Parse](#safe-parse-method)
6. [Basic Data Types](#basic-data-types)
7. [Tuples Types](#tuples-types)
8. [Union Types](#union-types)
9. [Record Types](#record-type)
10. [Map Types](#map-type)
11. [Set Types](#set-type)
12. [Promise Types](#promise-type)
13. [Error Handling](#error-handling)

## installation

```bash
pnpm add zod

```

## Basic Usage

create schema of a object and parse it to using parse

```ts
const UserSchema = z.object({
  name: z.string(),
  age: z.number(),
});

const user = {
  name: "deepak",
  age: 45,
};
console.log(UserSchema.parse(user));
```

## infer with zod type

usually in typescript we have to define types of every data, but we can **infer** with zod types so you don't need to define multiple times.

```ts
type User = z.infer<typeof UserSchema>;

const user: User = {
  name: "deepak",
  age: 32,
};
```

## parse method

this is a mehtod to parse the data with zod schmea.

```ts
console.log(UserSchema.parse(user));
```

## Safe Parse method

can be use to check the boolean state of parsing.

```ts
console.log(UserSchema.safeParse(user));
```

**the main diffrence between parse and safeParse is that parse will throw error and safeParse will return a object with success state and data value**

# Basic data types

zod support almost every data types.

```ts
const UserSchema = z.object({
  name: z.string(),
  age: z.number(), // or bigint()
  date: z.date(),
  isProgram: z.boolean(),
  test: z.undefined(),
  salary: z.null(),
  returnFunction: z.void(),
  other: z.unknown(), // can be anything
  isProgrammer: z.literal(true), // it must be this value
  hobbies: z.enum(["program", "coder", "skilled"]), // enum
});
```

**By default all the data value are required**

## data validatons

in zod all data values have their own validations

```ts
const UserSchema = z.object({
  name: z.string().min(3).max(25).default("hello").optional(),
  age: z.number().gt(0).lt(100), // or bigint()
  isProgrammer: z.boolean().nullable(), // it can be null
  //isProgrammer: z.boolean().nullish(),   // it can be null of undefined
});
```

## other schema validations

```ts
schmea.partial(); // it will make all the fields optional
schema.pick({ value: true }); // pick certain keys from a schema. cane be use to decalre a new schema from existing schema
schema.omit({ value: true }); // use to remove key from schema
schema.extend({new key:type}) // extend the schema with new value
schema.merge({new schema}) //merge two schema
```

### what happens when you pass some value to the schema which is no availabe in schema ?

**it will only return the value that is available in schema and any other value will be ignored**

---

**But we can use pass throught poroperty to pass the extra value**

```ts
schemaz.object({}).passthrough();
```

or you can use strict property to not passing any other extra data.

```ts
schemaz.object({}).strict();
```

# Array Types in zod

```ts
//simple usage
friends: z.array(z.string());
friends: ["f1", "f2"];
```

**the main difference between array and tuples is that, in tuples all values must be unique**

## tuples types

tuples are **fixed size array** with fix data types

```ts
coords: z.tuple([z.number(), z.number()]); // only accept two unique numbers.
coords = [23, 45];

coords: z.tuple([z.number()]).rest(z.number); // anything can be accepted
```

## union types

the union types to define multiple type to single variable

```ts
uuid: z.union([z.string(), z.number()]),
  // or use
uuid: z.string().or(z.number()),
uuid: "23", // or 23
```

## Record type

the record type can be use with map functions where you knew that there is a id but don't know the type

```ts
const UserSchema = z.record(z.string());
const userData: User = {
  uuid: "23",
  asd: "as",
};
```

## **if you want to define keys and the value**

frist value is a key and the second is the value

```ts
const UserSchema = z.record(z.string(), z.number());
const userData: User = {
  uuid: 23,
  asd: 45,
};
```

**always use map type for map**

## map type

```ts
const UserSchema = z.map(z.string(), z.object({ name: z.string() }));
const userData: User = new Map([
  ["data", { name: "hello" }],
  ["data1", { name: "world" }],
]);
```

## Set Type

```ts
const UserSchema = z.set(z.number());
const userData: User = new Set([1, 34, 5, 5, 5, 5]);
```

## Promise Type

the zod can have a promise type and return type from promise

```ts
const UserSchema = z.promise(z.string());
const userData: User = Promise.resolve("hi");
```

# Error handling

for error handling use zod-error-validation library. it gives really nice error messages
