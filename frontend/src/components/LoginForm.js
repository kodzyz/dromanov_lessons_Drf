//0:35 событие onChange
//привязка обработчика события к <input полю
//становится доступным набор в полях формы
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
            'login': event.target.value
        })
    }

    handlePasswordChange(event){
        this.setState({
            'password': event.target.value
        })
    }

    render () {
        return (
            <div>
                <form>
                    <input type="text" name="login" placeholder="login" value={this.state.login} onChange={(event) => this.handleChange(event)} />
                    <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event) => this.handlePasswordChange(event)} />
                    <input type="submit" value="Login" />

                </form>
            </div>
        )
    }
}
export default LoginForm;