--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-05-03 01:13:15 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 215 (class 1259 OID 16430)
-- Name: livro_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livro_codigo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livro_codigo_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16423)
-- Name: livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro (
    codigo bigint DEFAULT nextval('public.livro_codigo_seq'::regclass) NOT NULL,
    titulo character varying NOT NULL,
    sinopse character varying NOT NULL,
    autores character varying NOT NULL,
    editora character varying NOT NULL,
    edicao integer NOT NULL,
    genero character varying NOT NULL,
    numero_paginas character varying NOT NULL
);


ALTER TABLE public.livro OWNER TO postgres;

--
-- TOC entry 3441 (class 2606 OID 16429)
-- Name: livro livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro
    ADD CONSTRAINT livro_pkey PRIMARY KEY (codigo);


-- Completed on 2023-05-03 01:13:15 -03

--
-- PostgreSQL database dump complete
--

