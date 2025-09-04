import React, { useState, useEffect } from "react";
import axios from "axios";
import "./TaskDashboard.css";

const API_URL = "http://127.0.0.1:8000"; // FastAPI backend

export default function TaskDashboard() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [email, setEmail] = useState("");
  const [reminderTime, setReminderTime] = useState("");

  // Fetch tasks from backend
  const fetchTasks = async () => {
    try {
      const res = await axios.get(`${API_URL}/tasks/`);
      setTasks(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // Create a new task
  const createTask = async () => {
    try {
      await axios.post(`${API_URL}/tasks/`, {
        title,
        email,
        reminder_time: reminderTime,
      });
      fetchTasks();
      setTitle("");
      setEmail("");
      setReminderTime("");
    } catch (err) {
      console.error(err);
    }
  };

  // Delete a task
  const deleteTask = async (id) => {
    try {
      await axios.delete(`${API_URL}/tasks/${id}`);
      fetchTasks();
    } catch (err) {
      console.error(err);
    }
  };

  // JSX (HTML-like code)
  return (
    <div className="container">
      <h2>Task Dashboard</h2>
      <div>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="datetime-local"
          value={reminderTime}
          onChange={(e) => setReminderTime(e.target.value)}
        />
        <button onClick={createTask}>Add Task</button>
      </div>
      <h3>Tasks</h3>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            <span>
              {t.title} - {t.email} - {t.reminder_time} - {t.status}
            </span>
            <button onClick={() => deleteTask(t.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
