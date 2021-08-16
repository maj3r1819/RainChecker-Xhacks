import React from 'react'

function Wishlist_item(props) {
    return (
        <li className="todo stack-small" id={props.id}>
              <div className="c-cb">
                <label className="todo-label" htmlFor={props.id}>
                  {props.name}
                </label>
              </div>
              <div className="btn-group">
                <button type="button" className="btn">
                  Edit <span className="visually-hidden">{props.name}</span>
                </button>
                <button type="button" className="btn btn__danger" onClick={() => props.deleteTask(props.id)}>
                  Delete <span className="visually-hidden">{props.name}</span>
                </button>
              </div>
            </li>
    )
}

export default Wishlist_item
