// src/components/TodoList.js
import React, { Component } from "react";
import ProjectsItem from "./ProjectsItems";

export default class ProjectsList extends Component {
  render() {
    const {items, handleEdit ,  handleDelete }=this.props;
    return (
      <ul className="list-group my-2">
        {items.map((item)=>{
          return 
          <ProjectsItem 
          item={item} 
          handleEdit={handleEdit}
          handleDelete = {handleDelete}
           />
        })}
        
      </ul>
    );
  }
}