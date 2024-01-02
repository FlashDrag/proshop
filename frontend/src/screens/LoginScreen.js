import React, { useState, useEffect } from "react";
import { Link, redirect, useNavigate, useSearchParams } from "react-router-dom";
import { Form, Button, Row, Col, Alert } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import FormContainer from "../components/FormContainer";
import { login } from "../actions/userActions";

function LoginScreen() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = useDispatch();

  // get redirect query param from url
  const [searchParams, setSearchParams] = useSearchParams();
  const redirect = searchParams.get('redirect') || '/';

  const userLogin = useSelector(state => state.userLogin)
  const {error, loading, userInfo} = userLogin;

  // if user is logged in (userInfo is not null in redux store),
  // redirect to the page they were on before,
  // otherwise redirect to home
  const navigate = useNavigate();
  useEffect(() => {
    if (userInfo) {
      navigate(redirect);
    }
  }, [navigate, userInfo, redirect])

  // submitHandler dispatches login action with email and password
  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(login(email, password))
  };

  // TODO: add required to required fields after I complete testing backend required fields functionality
  return (
    <FormContainer>
      <h1>Sign In</h1>
      {error && error.detail && <Message variant='danger'>{error.detail}</Message>}
      {loading && <Loader size={50} />}

      <Form onSubmit={submitHandler}>
        <Form.Group controlId="email">
          <Form.Label>Emal Address</Form.Label>
          {error && error.email && <Alert className='p-0 text-danger bg-transparent border-0'>{error.email}</Alert>}
          <Form.Control
            required
            type="email"
            placeholder="Enter Email"
            value={email}
            {...(error && error.email && {isInvalid: true})}
            onChange={(e) => setEmail(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group controlId="password" className="py-3">
          <Form.Label>Password</Form.Label>
          {error && error.password && <Alert className='p-0 text-danger bg-transparent border-0'>{error.password}</Alert>}
          <Form.Control
            required
            type="password"
            placeholder="Enter Password"
            value={password}
            {...(error && error.password && {isInvalid: true})}
            onChange={(e) => setPassword(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Button type="submit" variant="primary">
          Sign In
        </Button>
      </Form>

      <Row className="py-3">
        <Col>
          New Customer?
          <Link
            to={redirect ? `/register?redirect=${redirect}` : "/register"}
            className="ps-2"
          >
            Register
          </Link>
        </Col>
      </Row>
    </FormContainer>
  );
}

export default LoginScreen;
