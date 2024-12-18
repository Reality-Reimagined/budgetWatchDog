import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import RequestReport from './pages/RequestReport';
import Analytics from './pages/Analytics';
// import History from './pages/History';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="request-report" element={<RequestReport />} />
          <Route path="analytics" element={<Analytics />} />
          {/* <Route path="history" element={<History />} /> */}
        </Route>
      </Routes>
    </Router>
  );
}

export default App;