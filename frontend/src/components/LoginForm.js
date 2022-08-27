//0:39 обращаемся к параметру target ->name="login" или name="password"
import React from 'react'

class LoginForm extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'login': '',
            'password': ''
        }
    }

    handleChange(event){
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render () {
        return (
            <div>
                <form>
                    <input type="text" name="login" placeholder="login" value={this.state.login} onChange={(event) => this.handleChange(event)} />
                    <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event) => this.handleChange(event)} />
                    <input type="submit" value="Login" />

                </form>
            </div>
        )
    }
}
export default LoginForm;