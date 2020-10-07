import React from 'react';
import './App.css';

class App extends React.Component {

    constructor(){
        super();
        this.state = {
            snacks: [
                {
                    id: 1,
                    name: "cookies",
                    type: "sweet"
                },
                {
                    id: 2,
                    name: "oranges",
                    type: "fruit"
                },
                {
                    id: 3,
                    name: "chocolate",
                    type: "happiness"
                }
            ],
            defaultSnack: "Falafel"
        };
        this.addNewSnack = this.addNewSnack.bind(this);
    }

    render(){
        return (
            <div className="App">
                <Header dSnack={this.state.defaultSnack} />
                <SnackList snacks={this.state.snacks} snackCreated={ snack => this.addNewSnack(snack) }/>
                <Footer text="@copyright ASAC" />
            </div>
        );
    }

    addNewSnack(snack){
        // alert(snack.name);
        // this.state.snacks.push({id:15, name:snack.name, type:snack.type});
        let allSnacks = this.state.snacks;
        allSnacks.push({id:15, name:snack.name, type:snack.type});
        this.setState({
            snacks: allSnacks
        });
    }
}


class SnackForm extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name: "",
            snackType: ""
        };
        this.handleChangeName = this.handleChangeName.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }

    // Fix Render
    render(){
        return(
            <form onSubmit={this.handleSubmit}>
                <label> Snack Name
                    <input type="text" placeholder="name" onChange={this.handleChangeName}></input>
                    <input type="text" placeholder="type"></input>
                    <input type="submit" value="Add"></input>
                </label>
            </form>
        )
    }

    handleChangeName(event){
        console.log("text entered to text input");
        let newName = event.target.value;
        this.setState({
            name: newName
        });
    }


    // ToDo
    // handleChangeType(){

    // }

    handleSubmit(event){
        event.preventDefault();
        // alert(this.state.name);
        this.props.onSnackCreate(this.state);
    }
}


function SnackList(props){
    return (
        <>
            <h2>Snacks Length: {props.snacks.length}</h2>
            <ul>
                {props.snacks.map( snack => <Snack item={snack} key={snack.id}/> )}
            </ul>
            <SnackForm onSnackCreate={(data) => props.snackCreated(data)}/>
        </>
    );
}


function Snack(props){
    return <li>{props.item.name}</li>;
}


// function Header => props
// class Header => state and props

function Header(props){
    return <header><h3>Our default Snack: {props.dSnack}</h3></header>;
}

function Footer(props){
    return <footer><small>{props.text}</small></footer>;
}

export default App;
