import React, { Component } from 'react';
import Navbar from './Navbar'
import RecipeItem from './RecipeItem'
import recipes from '../sample_data/recipes.json'
 
class App extends Component {
  constructor(props) {
    super(props);

    this.recipes = recipes.results;
    this.state = {
      searchString: '',
      itens: []
     }

    this.ChangeSearchString = this.ChangeSearchString.bind(this)
  }

  componentWillMount(){
    this.setState({ itens: recipes.results.map((item) => {return (<RecipeItem item = {item} search={''} />)})})
  }


  ChangeSearchString(string){
    
    let callback = () => {this.setState({itens: recipes.results.map(this.renderRecipeItem.bind(this)).filter((i) => {return i !== ''})})}
    this.setState({searchString: string},callback)
    }

  renderRecipeItem(item){
    
    if(this.state.searchString === '')
      return (<RecipeItem item = {item} search = {this.state.searchString} />)

    else if(item.title.toLowerCase().includes(this.state.searchString.toLowerCase()))
      return (<RecipeItem item = {item} search = {this.state.searchString}/>)
    
    else if (item.ingredients.toLowerCase().includes(this.state.searchString.toLowerCase()))
      return (<RecipeItem item = {item} search = {this.state.searchString}/>)
    
    else
      return ''
    
    
  }

  render() { 
    return (
      <div className="App">
        <Navbar callbackParent={(e) =>{this.ChangeSearchString(e.target.value)}} searchString={this.state.searchString}/>
        <div className="container mt-10">
          <div className="row">
            {
              this.state.itens.length === 0 &&
              <h1>No Results to Show</h1>
            }
            {this.state.itens.map((item) => {return(item)})}
            
          </div>
        </div>
      </div>
    );
  }
}

export default App;
