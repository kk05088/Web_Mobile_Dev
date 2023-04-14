import { useState } from "react";
import Task from "./task";
import ProjectForm from "./projectForm";

export default function ProjectPage() {
  const [taskList, setTaskList] = useState([]);
  const [editTitle ,setEditTitle] = useState("");

  function handleSubmit(e, task){
    e.preventDefault();
    
    setTaskList([...taskList, {
        title: task,
        id: Date.now()
    }]);
  }

  function handleEdit(id, newTitle) {
    const newTaskList = taskList.map((task) => {
      if (task.id === id) {
        return {
          ...task,
          title: newTitle
        }
      }
      return task;
    });
    setTaskList(newTaskList);
  }

  function handleDelete(id) {
    const newTaskList = taskList.filter((task) => task.id !== id);
    setTaskList(newTaskList);
  }
//   function idk(id){
//     const [editedTitle, newTitle] = useState("")


//   }

  return (
    <>
      <ProjectForm onSubmit={handleSubmit} />
      <hr/>
      
      {taskList.map((task, index)=> (
        <div key={task.id}>
          <Task 
            task={task} 
            index={index} 
            onEdit={handleEdit} 
            onDelete={handleDelete} 
          /> 
          <button onClick={() => 
            // {<form> <input value={editTitle} onChange={(e)=>setEditTitle(e.target.value)}> </input> </form>}

          handleEdit(task.id,"new title")
          }>Edit</button>
          <button onClick={() => handleDelete(task.id)}>Delete</button>
        </div>
      ))}
    </>
  );
}
