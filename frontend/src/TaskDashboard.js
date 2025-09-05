import React, { useEffect, useState } from "react";
import axios from "axios";
import "./TaskDashboard.css";

const API_URL = "http://127.0.0.1:8000";

function TaskDashboard() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [scheduledTime, setScheduledTime] = useState("");

  const token = localStorage.getItem("token");
  const axiosConfig = { headers: { Authorization: `Bearer ${token}` } };

  const fetchTasks = async () => {
    try {
      const response = await axios.get(`${API_URL}/tasks/`, axiosConfig);
      setTasks(response.data);
    } catch (err) {
      console.error("Error fetching tasks:", err);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const createTask = async (e) => {
    e.preventDefault();
    try {
      await axios.post(
        `${API_URL}/tasks/`,
        { title, scheduled_time: scheduledTime },
        axiosConfig
      );
      setTitle("");
      setScheduledTime("");
      fetchTasks();
    } catch (err) {
      console.error("Error creating task:", err);
    }
  };

  const deleteTask = async (taskId) => {
    try {
      await axios.delete(`${API_URL}/tasks/${taskId}`, axiosConfig);
      fetchTasks();
    } catch (err) {
      console.error("Error deleting task:", err);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  return (
    <div className="dashboard-container">
      <h1>Task Dashboard</h1>
      <button onClick={logout}>Logout</button>

      <form onSubmit={createTask}>
        <input
          type="text"
          placeholder="Task Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          type="datetime-local"
          value={scheduledTime}
          onChange={(e) => setScheduledTime(e.target.value)}
          required
        />
        <button type="submit">Add Task</button>
      </form>

      <h2>Your Tasks</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <strong>{task.title}</strong> -{" "}
            {new Date(task.scheduled_time).toLocaleString()}
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TaskDashboard;
