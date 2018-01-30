﻿import React from 'react';
import SearchTips from '../components/search-tips';

const SearchForm =
  (props) =>
    (
      <section>
        <h1>Поисковые подсказки</h1>
        <input
          className="search-input"
          type="search"
          onChange={(event) => props.onSearch(event.target.value)}
        />
        <SearchTips
          tips={props.tips}
        />
      </section>
    );

export default SearchForm;
