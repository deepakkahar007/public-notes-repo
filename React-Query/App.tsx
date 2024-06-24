import { useState } from "react";
import Post1 from "./components/post1";
import Post2 from "./components/post2";
import Post3 from "./components/post3";

function App() {
  const [Post, setPost] = useState(<Post1 />);

  return (
    <>
      <h1 className="uppercase text-center text-7xl underline">
        Tanstack React Query
      </h1>

      <button
        onClick={() => setPost(<Post1 />)}
        className="border p-2 mx-6 hover:bg-indigo-400 text-black"
      >
        go to post 1
      </button>

      <button
        onClick={() => setPost(<Post2 />)}
        className="border p-2 mx-6 hover:bg-indigo-400 text-black"
      >
        go to post 2
      </button>

      <button
        onClick={() => setPost(<Post3 />)}
        className="border p-2 mx-6 hover:bg-indigo-400 text-black"
      >
        get a post by id
      </button>
      {Post}
    </>
  );
}

export default App;

// const Users: { id: number; name: string }[] = [
//   { id: 1, name: "first" },
//   { id: 2, name: "second" },
//   { id: 3, name: "third" },
// ];

// function Wait(duration: number) {
//   return new Promise((resolve) => setTimeout(resolve, duration));
// }

// function App() {
//   const query = useQuery({
//     queryKey: ["user"],
//     queryFn: ({ queryKey }) =>
//       Wait(2000).then(() => {
//         console.log(queryKey);

//         return [...Users];
//       }),
//   });

//   if (query.status === "success") {
//     console.log("success");
//   }
