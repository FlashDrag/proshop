import React from "react";
import { Spinner } from "react-bootstrap";

function Loader({ size = 100 }) {
  return (
    <Spinner
      animation="border"
      role="status"
      style={{
        height: `${size}px`,
        width: `${size}px`,
        margin: "auto",
        display: "block",
      }}
    >
      <span className="sr-only">Loading...</span>
    </Spinner>
  );
}

export default Loader;
