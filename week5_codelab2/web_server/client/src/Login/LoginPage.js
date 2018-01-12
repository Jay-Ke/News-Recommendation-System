import React from 'react';

import LoginForm from './LoginForm';

class LoginPage extends React.Component{
    constructor(props){
        super(props);

        this.state={
            errors:'',
            user:{
                email:'',
                password:''
            }
        };
    }

    processForm(event){
        event.preventDefault();

        const email=this.state.user.email;
        const password=this.state.user.password;

        console.log(email);
        console.log(password);

        //TODO
    }

    changeUser(event){
        const field=event.target.name;
        const user=this.state.user;
        user[field]=event.target.value;

        this.setState({user});
    }

    render(){
        return (
            <LoginForm
            onSubmit={(e)=>this.processForm(e)}
            onChange={(e)=>this.changeUser(e)}
            errors={this.state.errors}
            user={this.state.user}
            />
        );
    }
}

export default LoginPage;