import React from 'react'

class BookForm extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'title': '',
            'authors': []  // массив id
        }
    }

    handleChange(event){
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleSubmit(event) {
        //this.props.obtainAuthToken(this.state.login, this.state.password)
        //console.log(this.state.login, this.state.password) // что сохранилось в состоянии при нажатии на Login
        event.preventDefault() // запрет событий по умолчанию в браузере
    }

    render () {
        return (
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="title" value={this.state.title} onChange={(event) => this.handleChange(event)} />
                    <select multiple>
                        {this.props.authors.map((author) => <option value={author.id}>{author.first_name} {author.last_name}</option> )}
                    </select>
                    <input type="submit" value="Create" />

                </form>
            </div>
        )
    }
}
export default BookForm;