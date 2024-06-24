# Tanstack React Query

1. [Installation](#installation)
2. [Initial Setup](#initial-setup)
3. [useQuery Hooks](#usequery-hooks)
   - [Loading State](#loading-and-error-state)
4. [Handle Url Params](#handle-url-params)
5. [Fresh Data](#to-see-the-fresh-data-in-page)
6. [Refetch Interval](#refetch-interval)
7. [Queries chaning](#to-check-and-chaining-multiple-quries-togather)
8. [use Mutations](#use-mutations)

### installation :

```bash
pnpm add @tanstack/react-query @tanstack/react-query-devtools

```

### Initial Setup

```ts
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

const query = new QueryClient({
  defaultOptions: {
    queries: {
      networkMode: "offlineFirst",
    },
    mutations: {
      networkMode: "offlineFirst",
    },
  },
});

<QueryClientProvider client={query}>
  <App />
  <ReactQueryDevtools />
</QueryClientProvider>;
```

## UseQuery Hooks:

the useQuery Hooks to get data and run async functions

```ts
import { useQuery, useMutation } from "@tanstack/react-query";

const query = useQuery({
  queryKey: ["user"],
  queryFn: () => Wait(2000).then(() => [...Users]),
});

console.log(query.data);
```

the QueryKey is just array of uniquly identifier for every query.
the Queryfn is async function to fetch data, it will always return promise

### Loading and Error state:

```ts
{query.isError ? <pre>{JSON.stringify(query.error)}</pre> : ""}

{query.isLoading ? <h1>Loading ...</h1 : "">}

```

### UseMutation Hooks :

the use mutation hooks can be use to send data to server.

```tsx
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";

const mutation = useMutation({
  mutationFn: async (name: string) => {
    return Wait(2000).then(() => Users.push({ id: 4, name }));
  },
});

<button
  onClick={() => mutation.mutate("fourth")}
  className="border border-indigo-900"
>
  add new user
</button>;
```

==the mutation functions doesnt update the data instantly==

**to instantly show the updated data use queryclient invalidatequeries functions**

```tsx
import { useQueryClient } from "@tanstack/react-query";

const mutation = useMutation({
  mutationFn: async (name: string) => {
    return Wait(2000).then(() => Users.push({ id: 4, name }));
  },
  onSuccess: () => {
    queryClient.invalidateQueries(["user"]);
  },
});
```

**the invalidateQueries(["enter a query key"])**

## handle url params

- /post = ("/post")
- /post/1 = ( "/post/id" )
- /post/category/1 = ("/post/{category:1})
- /post/1/comments = ("/post/id /{where:{comment :true}})

**the queryfn have a obj value to print that object use**

```ts
  queryFn: (obj) =>
      Wait(2000).then(() => {
        console.log(obj);

        return [...Users];
      }),
```

**this object have important value qith querykey and the query key can be use with paramesters for url handler**

### another way to check status of query

```ts
const query = useQuery({
  queryKey: ["user"],
  queryFn: ({ queryKey }) =>
    Wait(2000).then(() => {
      console.log(queryKey);

      return [...Users];
    }),
});

if (query.status === "success") {
  console.log("success");
}
```

### check the fetch status using

```ts
data.fetchStatus === "fetching"; // fetching data items
data.fetchStatus === "idle"; // fetched all data
data.fetchStatus === "paused"; // interupt by internet connections
```

## to see the fresh data in page

change stale time of default optuions of query data
it ca be set to every single request or change the query client instances so every request can use this

```ts
const query = new QueryClient({
  defaultOptions: {
    queries: {
      networkMode: "always",
      staleTime: 1000 * 60 * 5,   // this is 5 min stale time
    },
```

## Refetch Interval

this can be use to create dashoard where you need to see the latest data items in real time.

```ts
const data = useQuery({
  queryKey: ["post"],
  queryFn: Posts,
  refetchInterval: 2000, // this will refetch the data in every 2 sec
});
```

## to check and chaining multiple quries togather

you can use enabled method in useQuery to chain and dependent one query to another.

```ts
const id = undefined;
const data = useQuery({
  queryKey: ["post", id],
  queryFn: () => PostById(id),
});

const user = useQuery({
  queryKey: ["user", data?.data?.id], // passing value from data query
  enabled: data?.data?.id != null, // checking the query is exist or not
  queryFn: () => GetUser("deepak"), // executing the function if id was validate
});
```

## Use Mutations:
