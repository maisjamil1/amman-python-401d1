import React from 'react';
import './App.css';

class FoodChoice extends React.Component{
    constructor(){
        super();
        this.state = {
            // foods = [],
            foodChoice: "I don't know yet",
            hungerLevel: 0
        };
    }

    changeFood(favFood){
        console.log(favFood);
        // this.state["foodChoice"] = favFood;
        this.setState({
            foodChoice: favFood
        });
    }

    checkHungerLevel(){
        let level;

        if (this.state.foodChoice === "Sajeyeh"){
            level = 100;
        } else if (this.state.foodChoice === "Shawerma"){
            level = 50;
        } else {
            level = 1;
        }

        this.setState({
            hungerLevel: level
        });
    }

    render(){
        console.log(this.state.hungerLevel);
        return (
            <>
                <h1>Food Choices</h1>
                <button onClick={ () => this.changeFood("Shawerma")}> Shwerma</button>
                <button onClick={ () => this.changeFood("Sajeyeh")}> Sajeyeh</button>
                <button onClick={ () => this.changeFood("Falafel")}> Falafel</button>

                <button onClick={ () => this.checkHungerLevel()}> Check Hunger Level</button>

                <h3>My fav food is: {this.state.foodChoice}</h3>
                <h3>My hunger level is: {this.state.hungerLevel}</h3>

            </>
        );
    }

}

function Footer(props) {
  console.log(props);
  // logic
  return (
    <footer className="Footer">
      <p>Copy Right Stuff for {props.name}</p>
      <span>{props.company}</span>
    </footer>
  );
}

function Main(props) {
  return (
    <main>
      <div className="Main">
        <h1>Hello CodeSandbox</h1>
        <h2>Start editing to see some magic happen!</h2>
        <p>{getName()}</p>
        <FoodChoice foodChoice = "Shawerma" />
      </div>
    </main>
  );
}
export default function App() {
  // const name = "Ali";
  // return <h1>Hi</h1>;
  return (
    <>
      <Main />
      {/* <FoodChoice foodChoice = "Shawerma" /> */}
      <Footer company="Code Fellows" name="Aziz"/>

    </>
  );
}

function getName() {
  return "Ali";
}
