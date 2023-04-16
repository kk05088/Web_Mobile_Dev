import { useState } from "react";

export default function ProjectForm({onSubmit}) {
  const [title, setTitle] = useState("");

  function handleChange(e) {
    setTitle(e.target.value);
  }

  function handleSubmit(e){
    onSubmit(e, title);
    setTitle("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <h1>Project Manager:</h1>
      <label htmlFor="project-title">Task Title:</label>
      <input
        type="text"
        value={title}
        id="project-title"
        onChange={handleChange}
      />
      <button type="submit">Add</button>
    </form>
  );
}

