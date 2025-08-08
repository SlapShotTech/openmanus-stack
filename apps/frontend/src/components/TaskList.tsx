"use client";
import useSWR from 'swr';

type Props = {
  refresh: number;
};

const fetcher = (url: string) => fetch(url).then((res) => res.json());

export function TaskList({ refresh }: Props) {
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/api/tasks`,
    fetcher,
    { refreshInterval: 5000, revalidateOnFocus: false }
  );

  if (error) return <div>Error loading tasks</div>;
  if (!data) return <div>Loading tasks...</div>;

  return (
    <div>
      <h2 className="text-xl font-semibold mb-2">Tasks</h2>
      <ul className="space-y-2">
        {data.map((task: any) => (
          <li key={task.id} className="bg-slate-800 p-3 rounded">
            <span className="font-medium">{task.name}</span> —{' '}
            <span className="italic">{task.status}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}