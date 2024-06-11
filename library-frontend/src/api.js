// src/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Adjust the base URL according to your backend setup
});

export const getBooks = () => api.get('/bookse/');
export const deleteBook = (id) => api.delete(`/bookse/${id}/`);
