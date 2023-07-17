import React from "react";

const UserFavoriteAnimals = ({ favorites }) => 
  favorites.map((favorite, i) => <li key={i}>{favorite}</li>)

export default UserFavoriteAnimals