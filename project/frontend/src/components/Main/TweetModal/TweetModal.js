import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import Aux from '../../../hoc/Aux/Aux';
const TweetModal = ({ data }) =>
  !data.length ? (
    <Aux>
    <p>Nothing to show</p>
    </Aux>
  ) : (
    <Aux>
    <div className="column">
      <h2 className="subtitle">
      
        Showing <strong>{data.length} items</strong>
      </h2>
      <table className="table is-striped">
        <thead>
          <tr>
            {Object.entries(data[0]).map(el => <th key={key(el)}>{el[0]}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map(el => (
            <tr key={el.id}>
              {Object.entries(el).map(el => <td key={key(el)}>{el[1]}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </Aux>
  );
TweetModal.propTypes = {
  data: PropTypes.array.isRequired
};
export default TweetModal;