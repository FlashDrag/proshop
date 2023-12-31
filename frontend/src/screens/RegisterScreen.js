import React, { useState, useEffect } from "react";
import { Link, redirect, useNavigate, useSearchParams } from "react-router-dom";
import { Form, Button, Row, Col, Alert } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import FormContainer from "../components/FormContainer";
import { register } from "../actions/userActions";

function RegisterScreen() {

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordsMatchError, setPasswordsMatchError] = useState("");

  const dispatch = useDispatch();

  const [searchParams, setSearchParams] = useSearchParams();
  const redirect = searchParams.get('redirect') || '/';

  const userRegister = useSelector(state => state.userRegister)
  const {error, loading, userInfo} = userRegister;

  const navigate = useNavigate();
  useEffect(() => {
    if (userInfo) {
      navigate(redirect);
    }
  }, [navigate, userInfo, redirect])

  const submitHandler = (e) => {
    e.preventDefault();
    setPasswordsMatchError('');

    if (password != confirmPassword) {
      setPasswordsMatchError('Passwords do not match!');
    } else {
      dispatch(register(name, email, password))
    }
  };

  // TODO: add required to required fields after I complete testing backend required fields functionality
  // E.g: <Form.Control required></Form.Control>
  return (
    <FormContainer>
      <h1>Sign In</h1>
      {passwordsMatchError && <Message variant='danger'>{passwordsMatchError}</Message>}
      {error && error.detail && <Message variant='danger'>{error.detail}</Message>}
      {loading && <Loader size={50} />}
      <Form onSubmit={submitHandler}>

        <Form.Group controlId="name" className="py-1">
            <Form.Label>Name</Form.Label>
            {error && error.name && <Alert className='p-0 mb-0 text-danger bg-transparent border-0'>{error.name}</Alert>}
            <Form.Control
              type="name"
              placeholder="Enter Name"
              value={name}
              {...(error && error.name && {isInvalid: true})}
              onChange={(e) => setName(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="email" className="py-1">
              <Form.Label>Emal Address</Form.Label>
              {error && error.email && <Alert className='p-0 mb-0 text-danger bg-transparent border-0'>{error.email}</Alert>}
              <Form.Control
                type="email"
                placeholder="Enter Email"
                value={email}
                {...(error && error.email && {isInvalid: true})}
                onChange={(e) => setEmail(e.target.value)}
              ></Form.Control>
            </Form.Group>

          <Form.Group controlId="password" className="py-1">
            <Form.Label>Password</Form.Label>
            {error && error.password && <Alert className='p-0 mb-0 text-danger bg-transparent border-0'>{error.password}</Alert>}
            <Form.Control
              type="password"
              placeholder="Enter Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              {...(error && error.password && {isInvalid: true})}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="passwordConfirm" className="py-1">
            <Form.Label>Confim Password</Form.Label>
            {error && error.password && <Alert className='p-0 mb-0 text-danger bg-transparent border-0'>{error.password}</Alert>}
            <Form.Control
              type="password"
              placeholder="Repeat Password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              {...(error && error.password && {isInvalid: true})}
            ></Form.Control>
          </Form.Group>

          <Button type="submit" variant="primary" className="mt-1">
            Sign Up
          </Button>

      </Form>

      <Row className="py-3">
        <Col>
          Have an Account?
          <Link
            to={redirect ? `/login?redirect=${redirect}` : "/login"}
            className="ps-2"
          >
            Sign In
          </Link>
        </Col>
      </Row>

    </FormContainer>
  )
}

export default RegisterScreen;