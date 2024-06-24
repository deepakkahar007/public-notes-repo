import axios from "axios";

export default async function Posts() {
  return axios.get(`http://localhost:3000/post`).then((res) => res.data);
}

export async function PostById(id: number) {
  return {
    id: id,
    msg: `your id is ${id}`,
  };
}

export async function GetUser(user: string) {
  const data = {
    name: user,
    msg: `username ${user} is active`,
  };

  return data;
}
