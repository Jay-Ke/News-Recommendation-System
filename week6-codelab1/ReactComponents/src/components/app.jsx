import React, { Component } from 'react';

import SearchBar from './search_bar.jsx'

export default class App extends Component {
    constructor() {
        super();
        this.state = { fromSearchBar: 'initial value'};
    }

    getResultFromSearchBar(term) {
        this.setState({ fromSearchBar: term});
    }

    render() {
        return (
            <div>
                <div className="row">
                    <div className="col-md-8 col-md-offset-2">
                        <SearchBar
                            sendToApp={
                                (term) => {
                                    this.getResultFromSearchBar(term);
                                }
                            }
                        />
                    </div>
                </div>
                <div className="row">
                    <p>In App component: {this.state.fromSearchBar}</p>
                </div>
            </div>
        )
    }
}