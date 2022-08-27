//0:33 связывание состояния с формой(при изменении текстового поля изменяется состояние и наоборот)
//привязываем состояние к переменной value=
// Warning: You provided a `value` prop to a form field without an `onChange` handler
import React from 'react'

class LoginForm extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'login': '',
            'password': ''
        }
    }

    render () {
        return (
            <div>
                <form>
                    <input type="text" name="login" placeholder="login" value={this.state.login} />
                    <input type="password" name="password" placeholder="password" value={this.state.password} />
                    <input type="submit" value="Login" />

                </form>
            </div>
        )
    }
}
export default LoginForm;