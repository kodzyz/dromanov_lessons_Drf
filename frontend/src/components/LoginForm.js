//0:43 нажатие на кнопку Login вызывает перезагрузку приложения js
//запретим кнопке работать как submit - выполнение GET запроса

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

    handleSubmit(event) {
        console.log(this.state.login, this.state.password) // что сохранилось в состоянии при нажатии на Login
        event.preventDefault() // запрет событий по умолчанию в браузере
    }

    render () {
        return (
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name="login" placeholder="login" value={this.state.login} onChange={(event) => this.handleChange(event)} />
                    <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event) => this.handleChange(event)} />
                    <input type="submit" value="Login" />

                </form>
            </div>
        )
    }
}
export default LoginForm;