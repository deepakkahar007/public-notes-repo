# Prisma Notes

# table of content

1. [install all dependencies](#install-all-dependencies)
2. [create a tsconfg.json file](#create-a-tsconfgjson-file)
3. [initalize the prisma](#initalize-the-prisma)
4. [prisma built-in code formatter](#prisma-built-in-code-formatter)
5. [define models](#define-models)
6. [migrate model / schema with your database](#migrate-model--schema-with-your-database)
7. [prisma client](#prisma-client)
8. [CRUD operations](#crud-opertions)
9. [Model Fields](#model-fields)
10. [type modifiers](#type-modifiers)
11. [relationship](#relationships)

## install all dependencies :

```bash
yarn add --dev typescript prisma @prisma/client nodemon @types/node ts-node
```

## create a tsconfg.json file :

tsconfig.json file:

```json
{
  "compilerOptions": {
    "sourceMap": true,
    "outDir": "dist",
    "strict": true,
    "lib": ["ESNext"],
    "esModuleInterop": true
  }
}
```

## initalize the prisma

```bash
yarn prisma init --datasource-provider postgresql
```

the datasource-provider flag shows what database you are using and create files according to that.

## prisma built-in code formatter

```bash
yarn prisma format
```

## define models

```ts
model User{
  id Int @id @default(autoincrement())
  name String
}
```

in prisma model, every model should have a id or unique field to identify.

## migrate model / schema with your database

```bash
yarn prisma migrate dev --name init
```

use migrate only if you don't need any other optional flags.

## prisma client

whenever the migrations done the prisma will create a new prisma client. it will automatically install prisma/client but we already installed with other dependencies.

### to generate a new client use:

```bash
yarn prisma generate
```

# interact with database

## CRUD opertions:

```js
const create = await prisma.user.create({ data: { name: "provide name" } });
console.log(create);
const all = await prisma.user.findMany();
console.log(all);
const del_id = await prisma.user.delete({ where: { id: 3 } });
console.log(del_id);
const upd_id = await prisma.user.update({
  where: { id: 2 },
  data: { ...name:"new name" },
});
console.log(upd_id);
```

## model fields :

```ts
model User {
  id   Int    @id @default(autoincrement())
  id String @id @default(uuid())  // to create uuid
  id String @id @default(cuid())  // use cuid
  name String
  email String?   // optional fields
  rating Float    //float fields
  created_At DateTime   //datetime fields
  shared Json   //json fields
  favorite post[]   //array fields
}
```

note - not all database support json field postgresql does sqlite don't

# type modifiers

prisma support only two type modifiers :

1. ? = to create optional field
   user String?
2. [] = to create array field
   posts Int[]

# Relationships

to create a relationship between tables

```ts
model User{
  Post Post[]
}

model Post{
  User  User   @relation(fields: [author], references: [id])
  author Int
}
```
