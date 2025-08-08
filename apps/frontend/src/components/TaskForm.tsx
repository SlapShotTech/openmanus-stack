"use client";
import { useState } from 'react';

type Props = {
  onCreated?: () => void;
};

export function TaskForm({ onCreated }: Props) {
  const [name, setName] = useState('');
  const [goal, setGoal] = useState('');
  const [loading, setLoading] = useState(false);

  const createTask = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, goal }),
      });
      if (res.ok) {
        setName('');
        setGoal('');
        onCreated && onCreated();
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-800 p-4 rounded-lg mb-4">
      <input
        className="w-full p-2 mb-2 rounded bg-slate-700 text-white"
        placeholder="Task name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <textarea
        className="w-full p-2 mb-2 rounded bg-slate-700 text-white"
        placeholder="Goal"
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
      />
      <button
        className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded disabled:opacity-50"
        onClick={createTask}
        disabled={loading}
      >
        {loading ? 'Creating...' : 'Create Task'}
      </button>
    </div>
  );
}