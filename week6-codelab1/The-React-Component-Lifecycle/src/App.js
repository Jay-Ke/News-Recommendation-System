import React, { Component } from "react";
import Counter from "./Counter";

class App extends Component {
  //MOUNTING
  constructor(props) {
    super(props);
    this.state = {
      counter: 0
    };
  }

  incrementCounter = () => {
    this.setState({
      counter: ++this.state.counter
    });
  };

  //MOUNTING & UPDATING
  render() {
    return (
      <div>
        <Counter counter={this.state.counter} />
        <button onClick={this.incrementCounter}>Click1</button>
      </div>
    );
  }
}

export default App;
