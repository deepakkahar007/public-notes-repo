import { useQuery } from "@tanstack/react-query";
import Posts from "../api/post";

const post2 = () => {
  const data = useQuery({
    queryKey: ["post"],
    queryFn: Posts,
  });

  if (data.isLoading)
    return <h1 className="text-7xl text-center">Loading ....</h1>;

  if (data.isError)
    return (
      <pre className="text-2xl text-red-700 text-center">
        {JSON.stringify(data.error)}
      </pre>
    );

  return (
    <div className="flex justify-center items-center flex-col gap-8">
      <h1 className="text-5xl uppercase text-center mx-4">showing post 2</h1>
      {data.data.map((i: any) => {
        return (
          <div key={i.id} className="max-w-64 border ">
            <h1 className="font-bold text-xl">{i.title}</h1>
            <p className="text-blue-500">{i.desc}</p>
          </div>
        );
      })}
    </div>
  );
};

export default post2;
