import { useQuery } from "@tanstack/react-query";
import { PostById, GetUser } from "../api/post";

const post3 = () => {
  const id = 30;
  const data = useQuery({
    queryKey: ["post", id],
    queryFn: () => PostById(id),
  });

  const user = useQuery({
    queryKey: ["user", data?.data?.id],
    enabled: data?.data?.id != null,
    queryFn: () => GetUser("deepak"),
  });

  return (
    <div>
      <h1>{data.data?.msg}</h1>
      {user.isLoading ? <h1>loading ....</h1> : <h2>{user.data?.msg}</h2>}
    </div>
  );
};

export default post3;
