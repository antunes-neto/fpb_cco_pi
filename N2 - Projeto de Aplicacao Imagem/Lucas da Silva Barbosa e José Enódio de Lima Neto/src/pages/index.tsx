import type { NextPage } from "next";
import dynamic from "next/dynamic";

const DynamicComponentWithNoSSR = dynamic(
  () => import("../components/image-editor"),
  { ssr: false }
);

const Home: NextPage = () => {
  return (
    <div
      style={{
        width: "100vw",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#000",
      }}
    >
      <DynamicComponentWithNoSSR />
    </div>
  );
};

export default Home;
