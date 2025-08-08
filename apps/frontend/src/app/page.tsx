import { TaskList } from '../components/TaskList';
import { TaskForm } from '../components/TaskForm';
import { useState } from 'react';

export default function Home() {
  const [refresh, setRefresh] = useState(0);

  return (
    <main className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">OpenManus</h1>
      <TaskForm onCreated={() => setRefresh((r) => r + 1)} />
      <TaskList refresh={refresh} />
    </main>
  );
}