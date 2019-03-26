import React from 'react'
import Highlight from 'react-highlighter'

//"https://via.placeholder.com/350x300"
const RecipeItem = (props) => (
    <div className="col-sm-3 mt-4">
        <div className="card">
            <a href={props.item.href} target="_blank">
                <img className="card-img-top img-fluid" src={props.item.thumbnail} alt={props.item.title} />
            </a>
        <div className="card-body">
            <a href={props.item.href} target="_blank">
                <h5 className="card-title">
                    <Highlight search={props.search}>
                        {props.item.title}
                    </Highlight>
                </h5>
            </a>
                <p className="card-text">
                    <strong>Ingredients: </strong>
                    <Highlight search={props.search}>
                        {props.item.ingredients}
                    </Highlight>
                </p>
        </div>
        </div>
    </div>
)

export default RecipeItem;