import React, { Component } from 'react';
import './search_bar.css';

export default class SearchBar extends Component {
    constructor(props) {
        super(props);
        this.state = { term: '' };
    }

    render() {
        return (
            <form className="input-group search-bar" onSubmit={(e) => {
                e.preventDefault();
            }}
            >
                <i className="input-group-addon glyphicon glyphicon-search" aria-hidden="true"></i>
                <input className="form-control"
                    value={this.state.term}
                    onChange={
                        (event) => {
                            this.setState({ term: event.target.value});
                            this.props.sendToApp(event.target.value);
                        }
                    }
                />
                <span className="input-group-btn">
                    <button type="submit" className="btn btn-primay">
                        Search
                    </button>
                </span>
                <div className="row">In search bar component: {this.state.term}</div>
            </form>
        )
    }
}
