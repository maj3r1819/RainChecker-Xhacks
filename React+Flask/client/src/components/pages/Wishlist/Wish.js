import React, {useState} from 'react'
import './Wish.css'
import Wish_item from './wishlist-item'
import Form from './Form'
import FilterButton from './FilterButton'
import HeroSection from '../HeroSection'
import { homeObjOne } from './Data'
const { v4: uuidv4 } = require('uuid');

function Home() {

  function deleteTask(id) {
      const remainingTasks = tasks.filter(task => id !== task.id);
      console.log(remainingTasks.length);
    setTasks(remainingTasks);
  }

  
    function addTask(name) {
        const newTask = { id: uuidv4(), name: name, completed: false };
    setTasks([...tasks, newTask]);
  }

  const DATA = [
    { id: "todo-0", name: "Eat", completed: true },
    { id: "todo-1", name: "Sleep", completed: false },
    { id: "todo-2", name: "Repeat", completed: false }
  ];
  const [tasks, setTasks] = useState(DATA);


  const taskList = tasks.map(task => (
    <Wish_item 
    id={task.id}
     name={task.name} 
    completed={task.completed} 
    key={task.id}
     deleteTask={deleteTask}
    />
  ));

    return (
        <div className="todoapp stack-large">
          <h1>TodoMatic</h1>
          <Form addTask={addTask}/>
          <div className="filters btn-group stack-exception">
          <FilterButton />
          <FilterButton />
          <FilterButton />
          </div>
          <h2 id="list-heading">
            3 tasks remaining
          </h2>
          <ul
            role="list"
            className="todo-list stack-large stack-exception"
            aria-labelledby="list-heading"
          >
            {taskList}
            
          </ul>
        </div>
      );
    }

export default Home
