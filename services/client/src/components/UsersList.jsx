import React from 'react';

/**
 * Functional Component
 *
 * Functional components only render data that is passed in with props or state.
 * The data flows down, it's read only.
 */

const UsersList = props => {
  return (
    <div>
      {props.users.map(user => {
        return (
          <h4 key={user.id} className='box title is-4'>
            {user.username}
          </h4>
        );
      })}
    </div>
  );
};

export default UsersList;
