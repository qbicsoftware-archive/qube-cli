package life.qbic.portal.portlet

import com.liferay.portal.kernel.log.Log
import com.liferay.portal.kernel.log.LogFactoryUtil

/**
 * This class simulates a car engine startup routine by printing the corresponding sounds into the log. It functions as a litmus test for groovy support in the OSGi framework.
 *
 * @author Sven Fillinger
 * @since 1.10
 */
class GroovyCar {

  private static final Log log = LogFactoryUtil.getLog(GroovyCar.class)

  private static boolean engineOff = true

  static def start() {
    if (engineOff) {
      log.info("Starting engine...")
      log.info("Roaaarrrr!")
      engineOff = false
    } else {
      log.info("Engine is already running.")
    }
  }

}
