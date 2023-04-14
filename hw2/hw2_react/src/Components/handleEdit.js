import { useState } from "react";

export function useTaskEditor(task, taskList, setTaskList) {
  const [editTitle, setEditTitle] = useState(task.title);
  const [isEditing, setIsEditing] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();

    const newTaskList = taskList.map((t) => {
      if (t.id === task.id) {
        return {
          ...t,
          title: editTitle
        };
      }
      return t;
    });

    setTaskList(newTaskList);
    setIsEditing(false);
  }

  function handleCancel() {
    setIsEditing(false);
  }

  function handleEdit() {
    setIsEditing(true);
  }

  return {
    editTitle,
    setEditTitle,
    isEditing,
    handleSubmit,
    handleCancel,
    handleEdit
  };
}
