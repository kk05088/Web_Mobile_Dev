// src/App.js
import React, { Component, useState, useEffect } from "react";
import ProjectsInput from "./components/ProjectsInput";
import ProjectsList from "./components/ProjectsList";
import axios from "axios";


export default class App extends Component {
  state = {
    ProjectsList: [],
    activeItem:{
      title:"",
      completed : false,
    },
    editItem : false,
  };

  componentDidMount(){
    this.refreshList();
  }

  refreshList = ()=>{
    axios
    .get("api/v1/tasks")
    .then((res) => this.setState({ProjectsList:res.data.tasks}))
    .catch((err)=>console.log(err));
  }


  
  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };
    this.setState({ activeItem });
  };
  handleSubmit = (item) => {
    this.setState({
      editItem:false,
    });
    // alert("Save :: " + JSON.stringify(item));
    if (item._id){
      axios
      .patch(`/api/v1/tasks/${item._id}/`,item)
      .then((res)=>this.refreshList());
      return;
    }
    axios.post("/api/v1/tasks/",item).then((res)=> this.refreshList());
  };  

  handleEdit = (item)=>{
    this.setState({activeItem:item,editItem:true});
    // alert("edit ::"+JSON.stringify(item));
  };

  handleDelete = (item)=> {
    // alert("Delete ::" + JSON.stringify(item));
    axios
      .delete(`/api/v1/tasks/${item._id}/`)
      .then((res) => this.refreshList());
  };

  render() {
    return (
      <div className="container">
        <h1 className="text-uppercase text-center my-2">Project Manager App</h1>
        <div className="row">
          <div className="col-8 col-md-6 mx-auto mt-2">
            <ProjectsInput 
              activeItem={this.state.activeItem}
              editItem={this.state.editItem}
              handleChange={this.handleChange}
              handleSubmit={this.handleSubmit}
            />
            <ProjectsList 
            items={this.state.ProjectsList}
            handleEdit={this.handleEdit}
            handleDelete = {this.handleDelete}
            />
          </div>
        </div>
      </div>
    );
  }
}