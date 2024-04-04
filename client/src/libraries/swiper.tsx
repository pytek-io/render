import { registerComponent, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("swiper", async () => {
    const [swiper_react, swiper, _, _1, _2] = await Promise.all([
      import("swiper/react"),
      import("swiper"),
      import("swiper/css"),
      import("swiper/css/navigation"),
      import("swiper/css/lazy"),
    ]);
    const { Swiper, SwiperSlide } = await swiper_react;
    const { Navigation, Lazy } = await swiper;

    const MySwiper = React.forwardRef((props, ref) => {
      return (
        <Swiper
          modules={[Navigation, Lazy]}
          ref={ref}
          lazy={true}
          {...props}
        ></Swiper>
      );
    });
    registerComponent("Swiper", "", MySwiper, "swiper");
    registerComponent("SwiperSlide", "", SwiperSlide, "swiper");
  });
}
