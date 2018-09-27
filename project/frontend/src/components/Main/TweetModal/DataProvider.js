import React, { Component } from "react";
import PropTypes from "prop-types";

console.log(data);
class DataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  };
  state = {
      data: [],
      loaded: false,
      placeholder: "Loading..."
    };
  componentDidMount() {
    fetch(this.props.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" }, console.log('not working?'));
        }
        return response.json();
      })
      .then(data => this.setState({ data: data, loaded: true }, console.log('working finethis.state.data')));
  };
  render() {
    const { data, loaded, placeholder } = this.state;
    return loaded ? this.props.render(data) : <p>{placeholder}</p>;
  }
}
export default DataProvider;