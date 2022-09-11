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

    // метод обработки выбора автора
    handleAuthorsSelect(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'authors': []  // очищаем - пустой массив
            })
            return;
        }

        let authors = []

        for(let option of event.target.selectedOptions) {
            authors.push(option.value)
        }

        this.setState({
            'authors': authors
        })
        // test [1', '2']  массив выбранных id
    }

    handleSubmit(event) {
        this.props.createBook(this.state.title, this.state.authors)  // пробросили данные в App.js
        event.preventDefault()
    }

    render () {
        return (
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name="title" placeholder="title" value={this.state.title} onChange={(event) => this.handleChange(event)} />
                    <select multiple onChange={(event) => this.handleAuthorsSelect(event)}>
                        {this.props.authors.map((author) => <option value={author.id}>{author.first_name} {author.last_name}</option> )}
                    </select>
                    <input type="submit" value="Create" />

                </form>
            </div>
        )
    }
}
export default BookForm;